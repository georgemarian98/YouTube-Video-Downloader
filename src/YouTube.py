#pip install pytube
from pytube import YouTube
import os
import sys

def combine_audio(vidname, audname, outname, fps=25):
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)



def Download_video(url, option, output_directory):
    yt = YouTube(url)

    if os.path.isdir(output_directory) == False:
            os.mkdir(output_directory)

    if option == 0: #FullHD
        stream = yt.streams.filter(subtype="mp4").order_by('resolution').desc().first() #Video high rez
        video_fps = stream.fps
        stream.download()
        video_name = stream.default_filename

        stream = yt.streams.filter(only_audio=True).desc().first() #Audio high rez
        stream.download()
        
        audio_name = stream.default_filename
        output_name = output_directory + video_name

        combine_audio(video_name, audio_name, output_name,video_fps)

        os.remove(video_name)
        os.remove(audio_name)

    elif option == 1: # HD
        stream = yt.streams.filter(progressive=True).first().download(output_directory) #Video and audio

    elif option == 2: # Video Only
        stream = yt.streams.filter(subtype="mp4").order_by('resolution').desc().first().download(output_directory) #Video high rez
    
    elif option == 3: # Audio Only
         stream = yt.streams.filter(only_audio=True).desc().first().download(output_directory)
