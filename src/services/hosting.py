import os

import aiofiles
from fastapi import Response, status

CHUNK_SIZE = 1024 * 1024


async def read_video_range(range, path):
    start, end = range.replace("bytes=", "").split("-")
    start = int(start)
    end = int(end) if end else start + CHUNK_SIZE
    if not os.path.exists(path):
        return Response(
            None,
            status_code=status.HTTP_404_NOT_FOUND,
        )
    filesize = os.path.getsize(path)
    async with aiofiles.open(path, "rb") as file:
        await file.seek(start)
        data = await file.read(end - start)
        headers = {
            "Content-Range": f"bytes {str(start)}-{str(end)}/{filesize}",
            "Accept-Ranges": "bytes",
        }
    return Response(
        data,
        status_code=status.HTTP_206_PARTIAL_CONTENT,
        headers=headers,
        media_type="video/mp4",
    )
