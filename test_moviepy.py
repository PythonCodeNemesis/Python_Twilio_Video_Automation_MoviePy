from moviepy.editor import *

def create_video_template():
    # Set the duration and resolution of the video
    duration = 10  # seconds
    resolution = (1280, 720)

    # Create a new video clip with the given resolution
    video_clip = ColorClip(color=(255, 255, 255), size=resolution, duration=duration)

    # Add a text overlay
    text_clip = TextClip("Welcome to our video marketing campaign!", fontsize=40, color='white', bg_color='black')
    text_clip = text_clip.set_position(('center', 'center')).set_duration(duration)
    video_clip = CompositeVideoClip([video_clip, text_clip])

    # Add an image overlay
    image_clip = ImageClip("D://logo.jpg", duration=duration)
    image_clip = image_clip.set_position(('right', 'bottom')).set_duration(duration)
    video_clip = CompositeVideoClip([video_clip, image_clip])

    # Add a fade-in and fade-out effect
    video_clip = video_clip.fadein(2).fadeout(2)

    # Write the video clip to a file
    video_clip.write_videofile("video_template.mp4", codec="libx264", fps=30)

def generate_dynamic_video():
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



# Main execution
create_video_template()
generate_dynamic_video()
