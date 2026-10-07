from moviepy import VideoFileClip

# Caminhos de entrada e saída
input_path = r"C:\\Users\\ulyss\\Downloads\\vídeos\\Nastya e Papai.mp4" 
output_path = r"C:\\Users\\ulyss\\Downloads\\vídeossaida.avi"

# Carrega o vídeo
clip = VideoFileClip(input_path)

# Redimensiona para 128x160 pixels
clip_resized = clip.resized((128, 160))

# Exporta em formato AVI
clip_resized.write_videofile(
    output_path,
    codec="mpeg4",          # usa XVID compatível com AVI
    audio_codec="mp3",      # compressão de áudio
    bitrate="300k",         # taxa de bits reduzida
    audio_bitrate="64k",    # som leve
    threads=2,              # usa 2 núcleos apenas
    ffmpeg_params=["-vf", "scale=128:160", "-preset", "ultrafast", "-crf", "35"])

print("✅ Conversão concluída! Vídeo otimizado para YP3_2.0.43 (128x160, MJPEG AVI).")
