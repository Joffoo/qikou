import os
import sys
import win32com.client

sys.stdout.reconfigure(encoding="utf-8")


def text_to_wav(text: str, output_path: str):
    """通过 Windows 本地 SAPI 物理合成真实 16-bit 线性 PCM 音频"""
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    filestream = win32com.client.Dispatch("SAPI.SpFileStream")
    filestream.Open(output_path, 3, False)
    speaker.AudioOutputStream = filestream
    speaker.Speak(text)
    filestream.Close()
    return output_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.exists(target):
            with open(target, "r", encoding="utf-8") as f:
                content = f.read()
        else:
            content = target
    else:
        content = sys.stdin.read()

    if not content.strip():
        print("错误：未提供待测文本。")
        sys.exit(1)

    wav_file = os.path.abspath(
        sys.argv[2] if len(sys.argv) > 2 else "cadence.wav"
    )
    os.makedirs(os.path.dirname(wav_file), exist_ok=True)
    text_to_wav(content, wav_file)
    print(f"音频已生成: {wav_file}")
