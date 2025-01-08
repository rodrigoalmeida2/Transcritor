from salvar import SaveSummaries as ss
import transcricao as tr


if __name__ == "__main__":
    video_file = "kamala.mp4"  # caminho do vídeo
    texto = tr.processa_video(video_file)
    ss.save_to_word(texto)