from moviepy import VideoFileClip

# ======= CONFIGURAÇÃO DOS CAMINHOS =======
# Aqui você coloca o caminho completo (ou apenas o nome) do vídeo original.
# Exemplo: "C:/Videos/meu_video.mp4"  ou  "meu_video.mp4" se estiver na mesma pasta do script.
input_path = "C:\\Users\\ulyss\\Downloads\\vídeos\\Nastya e Papai.mp4"

# Aqui você define onde e com qual nome o vídeo convertido será salvo.
# Exemplo: "C:/Videos/saida.avi"
output_path = "C:\\Users\\ulyss\\Downloads\\vídeossaida.avi"
# ==========================================

# Carrega o vídeo de entrada
clip = VideoFileClip(input_path)

# Redimensiona o vídeo para 128x160 pixels
clip_resized = clip.resize((128, 160))

# Exporta o vídeo no formato AVI
clip_resized.write_videofile(output_path, codec="png", fps=clip.fps)