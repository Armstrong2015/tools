import os
import glob
from  moviepy.editor import *

inpath = "E:\BaiduNetdiskDownload\生活 第五季.[关注公众号@电影虾]"
outpath = "E:\BaiduNetdiskDownload\mp3"

for filename in glob.glob(inpath + "\*"):
	name = os.path.splitext(file)[0]
	savename = name + ".mp3"
	video = VideoFileClip(filename)
	audio = video.audio
	audio.write_audiofile(outpath + "\" + savename)