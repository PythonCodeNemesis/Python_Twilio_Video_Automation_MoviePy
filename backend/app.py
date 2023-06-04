from flask import Flask, request, jsonify
from twilio.rest import Client
from moviePy_twilio_utils import send_video_via_twilio, create_video_template

app = Flask(__name__)

def generate_dynamic_video_for_single_recipient(recipient_name, recipient_email):
    # Load the video template
    video_template = VideoFileClip("video_template.mp4")

    # Fetch recipient data (e.g., names, email addresses) from a database or API
    recipients = [
        {"name": "John Doe", "email": "john.doe@example.com"},
        {"name": "Jane Smith", "email": "jane.smith@example.com"}
    ]

    personalized_text = f"Hi {recipient_name}, this video is just for you!"
    personalized_text_clip = TextClip(personalized_text, fontsize=40, color='white', bg_color='black')
    personalized_text_clip = personalized_text_clip.set_position(('center', 'center')).set_duration(video_template.duration)
    personalized_video = CompositeVideoClip([video_template, personalized_text_clip])

    # Write the personalized video to a file
    video_filename = f"video_{recipient_name.lower().replace(' ', '_')}.mp4"
    personalized_video.write_videofile(video_filename, codec="libx264", fps=30)

    # Send the video to the recipient via Twilio
    send_video_via_twilio(video_filename, recipient_email)
    

def generate_dynamic_video_for_multiple_recipient(recipient):
    # Load the video template
    video_template = VideoFileClip("video_template.mp4")

    # Fetch recipient data (e.g., names, email addresses) from a database or API
    recipients = [
        {"name": "John Doe", "email": "john.doe@example.com"},
        {"name": "Jane Smith", "email": "jane.smith@example.com"}
    ]

    for recipient in recipients:
        # Customize the video template
        personalized_text = f"Hi {recipient['name']}, this video is just for you!"
        personalized_text_clip = TextClip(personalized_text, fontsize=40, color='white', bg_color='black')
        personalized_text_clip = personalized_text_clip.set_position(('center', 'center')).set_duration(video_template.duration)
        personalized_video = CompositeVideoClip([video_template, personalized_text_clip])
        
        # Write the personalized video to a file
        video_filename = f"video_{recipient['name'].lower().replace(' ', '_')}.mp4"
        personalized_video.write_videofile(video_filename, codec="libx264", fps=30)
        
        # Send the video to the recipient via Twilio
        send_video_via_twilio(video_filename, recipient['email'])

@app.route('/send-video', methods=['POST'])
def send_video():
    # Get recipient email and name from the request data
    recipient_email = request.json['email']
    recipient_name = request.json['name']

    # Generate the personalized video using MoviePy  
    generate_dynamic_video(recipient_name, recipient_email)
    
    # Use Twilio to send the personalized video to the recipient's email
    send_video_via_twilio(video_filename, recipient['email'])

    # Return a success message
    return jsonify({'message': 'Video sent successfully'})
  
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    return response

if __name__ == '__main__':
    app.run(debug=True)

