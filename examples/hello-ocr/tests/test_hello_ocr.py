from openfilter.filter_runtime import Filter
from openfilter.filter_runtime.filters.video_in import VideoIn
from openfilter.filter_runtime.filters.webvis import Webvis
from filter_optical_character_recognition.filter import FilterOpticalCharacterRecognition


def test_foo():
    pass

def test_stream_start_and_stops_successfully():
    runner_exit_codes = Filter.run_multi([
        (VideoIn, dict(
            sources='file://hello.mov',
            outputs='tcp://*:5550',
        )),
        (FilterOpticalCharacterRecognition, dict(
            sources='tcp://localhost:5550',
            outputs='tcp://*:5552',
            ocr_engine='easyocr',
            forward_ocr_texts=True,
        )),
        (Webvis, dict(
            sources='tcp://localhost:5552',
        )),
    ], exit_time=3)
    assert(runner_exit_codes == [0, 0, 0])
