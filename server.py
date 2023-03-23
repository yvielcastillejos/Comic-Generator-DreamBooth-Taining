from flask import Flask, render_template, request, session
import os
from werkzeug.utils import secure_filename
import json
import os
import subprocess
 
#*** Backend operation
 
# WSGI Application
# Defining upload folder path
UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
# # Define allowed files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
 
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name for template path
# The default folder name for static files should be "static" else need to mention custom folder for static path
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
# Configure upload folder for Flask application
 
# Define secret key to enable session
app.secret_key = 'This is your secret key to utilize session in Flask'
 
 
@app.route('/')
def index():
    return render_template('upload.html')
 
@app.route('/',  methods=("POST", "GET"))
def uploadFile():
    MODEL_NAME = "runwayml/stable-diffusion-v1-5"
    OUTPUT_DIR = "stable_diffusion_weights"
    if request.method == 'POST':
 
        # You can also add multiple concepts here. Try tweaking `--max_train_steps` accordingly.

        concepts_list = [
            {
                "instance_prompt":      "partyxyz girl",
                "class_prompt":         "girl",
                "instance_data_dir":    "./data/" + "partyxyzgirl",
                "class_data_dir":       "./data/girl"
            },
        ]

        os.mkdir(concepts_list["instance_data_dir"])
        os.mkdir(concepts_list["class_data_dir"])
        app.config['UPLOAD_FOLDER'] = concepts_list["instance_data_dir"]

        
        cmd = ["accelerate", "launch", "train_dreambooth.py",
            "--pretrained_model_name_or_path={}".format(MODEL_NAME),
            "--pretrained_vae_name_or_path=stabilityai/sd-vae-ft-mse",
            "--output_dir={}".format(OUTPUT_DIR),
            "--revision=fp16",
            "--with_prior_preservation", "--prior_loss_weight=1.0",
            "--seed=1337",
            "--resolution=512",
            "--train_batch_size=1",
            "--train_text_encoder",
            "--mixed_precision=no",
            "--use_8bit_adam",
            "--gradient_accumulation_steps=1",
            "--learning_rate=1e-6",
            "--lr_scheduler=constant",
            "--lr_warmup_steps=0",
            "--num_class_images=50",
            "--sample_batch_size=4",
            "--max_train_steps=1000",
            "--save_interval=200",
            "--save_sample_prompt=" + concepts_list["instance_prompt"],
            "--concepts_list=concepts_list.json"
            ]

        for c in concepts_list:
            os.makedirs(c["instance_data_dir"], exist_ok=True)

        with open("concepts_list.json", "w") as f:
           json.dump(concepts_list, f, indent=4)

        uploaded_files = request.files.getlist('uploaded-files[]')
        for file in uploaded_files:
           # Upload file flask
            
            # Extracting uploaded data file name
            img_filename = secure_filename(file.filename)
            # Upload file to database (defined uploaded folder in static path)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
            # Storing uploaded file path in flask session
            session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)

        subprocess.run(cmd, check=True)
    
        return render_template('index_upload_and_show_data_page2.html')
 
 

if __name__=='__main__':
    app.run(debug = True)