import subprocess
import whisper
import os

def extrai_audio(video_path, audio_output_path):
    """Extrai o áudio de um vídeo usando FFmpeg"""
    comando = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_output_path}"
    subprocess.run(comando, shell=True)
    return audio_output_path

def tamanho_video(video_path):
    # Obtém o tamanho do arquivo em bytes
    file_size = os.path.getsize(video_path)
    # Classifica o tamanho do vídeo em categorias
    if file_size < 75_000_000:
        return "tiny"
    elif 75_000_000 <= file_size < 140_000_000:
        return "base"
    elif 140_000_000 <= file_size < 460_000_000:
        return "small"
    else:
        return "large"

def transcreve_audio_whisper(audio_path, model_size):
    """Transcreve o áudio usando Whisper"""
    model = whisper.load_model("medium")  # Você pode usar 'tiny', 'base', 'small', 'medium', ou 'large' dependendo do desempenho necessário
    result = model.transcribe(audio_path)
    return result['text']  # Retorna o texto

def processa_video(video_path):
    # 1. Extrai áudio do vídeo
    audio_path = os.path.splitext(video_path)[0] + ".wav"
    extrai_audio(video_path, audio_path)
    
    # 2. Transcreve áudio usando Whisper
    tamanho_modelo = tamanho_video(video_path)
    text = transcreve_audio_whisper(audio_path, tamanho_modelo)
   
    return text


