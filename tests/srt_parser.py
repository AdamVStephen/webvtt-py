from .generic import GenericParserTestCase
from webvtt.exceptions import MalformedFileError, MalformedCaptionError


class SRTParserTestCase(GenericParserTestCase):

    def test_srt_parse_empty_file(self):
        self.assertRaises(
            MalformedFileError,
            self.webvtt.from_srt,
            self._get_file('empty.vtt')  # We reuse this file as it is empty and serves the purpose.
        )

    def test_srt_invalid_format(self):
        for i in range(1, 5):
            self.assertRaises(
                MalformedFileError,
                self.webvtt.from_srt,
                self._get_file('invalid_format{}.srt'.format(i))
            )

    def test_srt_total_length(self):
        self.assertEqual(
            self.webvtt.from_srt(self._get_file('sample.srt')).total_length,
            23
        )

    def test_srt_parse_captions(self):
        self.assertTrue(self.webvtt.from_srt(self._get_file('sample.srt')).captions)

    def test_srt_missing_timeframe_line(self):
        self.assertRaises(
            MalformedCaptionError,
            self.webvtt.from_srt,
            self._get_file('missing_timeframe.srt')
        )

    def test_srt_missing_caption_text(self):
        self.assertRaises(
            MalformedCaptionError,
            self.webvtt.from_srt,
            self._get_file('missing_caption_text.srt')
        )

    def test_srt_invalid_timestamp(self):
        self.assertRaises(
            MalformedCaptionError,
            self.webvtt.from_srt,
            self._get_file('invalid_timeframe.srt')
        )

    def test_srt_timestamps_format(self):
        self.webvtt.from_srt(self._get_file('sample.srt'))
        self.assertEqual(self.webvtt.captions[2].start_as_timestamp, '00:00:11.890')
        self.assertEqual(self.webvtt.captions[2].end_as_timestamp, '00:00:16.320')
