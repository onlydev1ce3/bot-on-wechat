import os
import shutil
from pydub import AudioSegment
import json
import os
import time

from aip import AipSpeech
from bridge.context import *
from bridge.reply import *
from channel.channel import Channel
from common.dequeue import Dequeue
from common import memory
from plugins import *


from bridge.reply import Reply, ReplyType
from common.log import logger
from common.tmp_dir import TmpDir
from config import conf
from voice.audio_convert import get_pcm_from_wav
from voice.voice import Voice
def any_to_wav(any_path, wav_path):
    """
    把任意格式转成wav文件
    """
    if not os.path.isfile(any_path):
        raise FileNotFoundError(f"The file {any_path} does not exist.")
    
    if any_path.endswith(".wav"):
        shutil.copy2(any_path, wav_path)
        return
    
    
    audio = AudioSegment.from_file(any_path)
    audio = audio.set_frame_rate(8000)    # 百度语音转写支持8000采样率, pcm_s16le, 单通道语音识别
    audio = audio.set_channels(1)
    audio.export(wav_path, format="wav", codec='pcm_s16le')

# 调用示例
try:
    any_to_wav("240628-155750.mp3", "output.wav")
    print("Conversion successful.")
except FileNotFoundError as e:
    print(e)
