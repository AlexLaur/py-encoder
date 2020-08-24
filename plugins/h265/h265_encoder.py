import os
import subprocess

from PySide2 import QtWidgets

from libs.plugin_collection import Plugin

SCRIPT_PATH = os.path.dirname(__file__)


class H265Encoder(Plugin):
    """This plugin convert files in H.265"""
    def __init__(self):
        super(H265Encoder, self).__init__()
        self.logger = None

        self.description = 'Convert any file in H.265'
        self.name = 'H.265/HEVC'
        self.extension = 'mp4'

    def perform_operation(self,
                          logger,
                          input_path,
                          output_path,
                          overwrite_output,
                          *args, **kwargs):
        self.logger = logger
        logger.info('Start conversion H.265/HEVC')

        status = False
        try:
            self.create_output_path(path=output_path)

            cmd = ['ffmpeg', '-i', input_path, '-c:v', 'libx265', output_path]
            sub = subprocess.Popen(cmd)
            sub.wait()

            # ffmpeg -i INPUT -c:v libx265 OUT.mov
            # stream = ffmpeg.input(input_path)
            # stream = ffmpeg.output(stream, output_path)
            # ffmpeg.run(stream, overwrite_output=overwrite_output)

            status = True
        except Exception as error:
            logger.error(error)
            status = False

        return status

    def create_output_path(self, path):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
