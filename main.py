import moviepy.editor as mp
import os

# Mengambil teks dari skrip cerita
with open('script.txt', 'r') as f:
    script_text = f.read()

# Menentukan path untuk gambar dan video
images_path = '/path/to/images/'
videos_path = '/path/to/videos/'

# Memecah teks skrip menjadi bagian-bagian
sections = script_text.split('\n\n')

# Membuat daftar klip video
clips = []

for section in sections:
    # Memecah setiap bagian menjadi sub-bagian
    sub_sections = section.split('\n')
    sub_clips = []
    for sub_section in sub_sections:
        # Memilih file gambar atau video sesuai dengan nama file yang terdapat pada sub-bagian skrip
        file_name = sub_section.strip() + '.mp4'
        if os.path.exists(os.path.join(videos_path, file_name)):
            sub_clips.append(mp.VideoFileClip(os.path.join(videos_path, file_name)))
        elif os.path.exists(os.path.join(images_path, file_name)):
            sub_clips.append(mp.ImageClip(os.path.join(images_path, file_name)))
    # Menggabungkan sub-bagian menjadi satu klip video
    clips.append(mp.concatenate_videoclips(sub_clips))

# Menggabungkan semua klip video menjadi satu video utuh
final_clip = mp.concatenate_videoclips(clips)

# Menyimpan video ke dalam file
final_clip.write_videofile('output.mp4')
