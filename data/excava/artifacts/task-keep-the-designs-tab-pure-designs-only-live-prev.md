# Keep the Designs tab pure: designs only, live previews, taste-ranked

> visual · task `keep-the-designs-tab-pur-83429` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

**Approach:**
Strip the Designs tab to a curated, taste-ranked gallery of live previews with zero fluff.

**Steps:**
1. **Audit & purge** – Run `find ./designs -type f \! -name "*.png" \! -name "*.jpg" \! -name "*.gif" \! -name "*.mp4" -delete` to delete non-media files in `/designs`.
2. **Rename & standardize** – Use `rename 's/.*/design-$1.jpg/' *.jpg` (adjust extension) to enforce `design-<id>.<ext>` naming.
3. **Generate live previews** – For each file, create a matching `.html` file (e.g., `design-123.html`) with an `<iframe>` embedding the live URL (e.g., `https://example.com/design-123`). Use a script like:
   ```bash
   for f in designs/*.jpg; do
     id=$(basename "$f" .jpg)
     cat > "designs/$id.html" <<EOF
   <!DOCTYPE html>
   <html><body>
     <iframe src="https://example.com/$id" style="width:100%;height:600px;border:none;"></iframe>
   </body></html>
   EOF
   done
   ```
4. **Rank & curate** – Manually sort files into subfolders (`/top-tier`, `/mid-tier`, `/experimental`) based on Chroma’s taste criteria (e.g., "no skeuomorphism," "bold color blocking").
5. **Update tab logic** – Modify the Designs tab’s navigation to
