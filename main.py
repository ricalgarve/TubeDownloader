import argparse
import yt_dlp


def main():
    parser = argparse.ArgumentParser(description="TubeDownloader - Download videos from the web")
    parser.add_argument("url", nargs="?", help="The URL of the video to download")
    parser.add_argument("--audio-only", action="store_true", help="Baixar apenas o áudio em MP3")
    parser.add_argument("--output", default="%(title)s.%(ext)s", help="Nome do arquivo de saída")

    args = parser.parse_args()

    # Se a URL não for passada por argumento, pede ao usuário
    video_url = args.url
    if not video_url:
        video_url = input("Cole a URL do vídeo aqui: ").strip()

    if not video_url:
        print("Erro: Nenhuma URL fornecida.")
        return

    if args.audio_only:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": args.output,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
    else:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": args.output,
            "merge_output_format": "mp4",
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Vídeo selecionado: {video_url}")

        # Busca informações sem baixar
        info = ydl.extract_info(video_url, download=False)
        print(f"Título: {info.get('title', 'N/A')}")
        print(f"Duração: {info.get('duration', 0)} segundos")

        # Inicia o download
        print("Baixando...")
        ydl.download([video_url])
        print("Download concluído!")


if __name__ == "__main__":
    main()
