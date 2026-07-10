# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-964` (dept) · 2026-07-10T02:04:39.376737+00:00
> Participants: Reel, Scriv, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement dual-path extraction for transcripts, utilizing both ffmpeg for embedded subtitles and Tesseract OCR for burned-in captions.

**Plan:**
1. Retrieve the pending video queue from the transcripts directory, filtering for `.mp4` and `.mov` files.
2. For each video, attempt to extract embedded captions using ffmpeg, generating a raw `.srt` file if extraction is successful.
3. If no embedded captions are found, apply Tesseract OCR on a frame of the video to capture any burned-in text.
4. Log the detection method used for each file, indicating whether embedded captions or OCR was utilized.
5. Compile output as raw SRT/JSON per video and maintain a comprehensive log of the entire process.

**What changed:** Added Tesseract OCR as a fallback for cases where subtitles are not extractable by ffmpeg.
