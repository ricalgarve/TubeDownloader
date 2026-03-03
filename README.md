# TubeDownloader

Script simples para baixar vídeos e áudios do YouTube (e outros sites) usando `yt-dlp`.

## Como usar

### Executável

Aqui você pode baixar a versão pronta para uso no Windows:

| Versão | Descrição | Download |
| :--- | :--- | :--- |
| **Windows (.exe)** | TubeDownloader Portable | [⬇️ Baixar Agora](https://github.com/ricalgarve/TubeDownloader/raw/main/dist/TubeDownloader.exe) |

Se você já baixou, siga os passos abaixo:
1. Abra o `TubeDownloader.exe`.
2. Cole o link do vídeo.
3. Aperte Enter.

### Script Python
Pra rodar direto no terminal:
```bash
pip install -r requirements.txt
python main.py
```

**Comandos extras:**
- `python main.py --audio-only`: Baixa só o áudio (converte pra MP3).
- `python main.py --output "nome_do_arquivo.mp4"`: Define o nome do arquivo.

## Requisito importante
Para baixar **MP3** ou vídeos em **alta resolução**, você precisa ter o **FFmpeg** instalado e configurado no PATH do Windows. Sem ele, a conversão ou a junção do vídeo com o áudio pode falhar.

---
Feito com [yt-dlp](https://github.com/yt-dlp/yt-dlp).
