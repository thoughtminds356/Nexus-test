from django.http import HttpResponse, Http404
from django.conf import settings
from django.utils._os import safe_join
import mimetypes
import os

def serve_media(request, path):
    """
    Serve media files with proper CORS headers and content types.
    This is especially important for SVG files.
    """
    try:
        # Construct the full path to the media file
        full_path = safe_join(settings.MEDIA_ROOT, path)
        
        if not os.path.exists(full_path):
            raise Http404("Media file not found")
            
        # Get the MIME type
        content_type, _ = mimetypes.guess_type(full_path)
        
        # Special handling for SVG files
        if path.lower().endswith('.svg'):
            content_type = 'image/svg+xml'
            
        # Read and serve the file
        with open(full_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type=content_type)
            
        # Add CORS headers
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept, Authorization'
        
        # Add caching headers for better performance
        response['Cache-Control'] = 'public, max-age=3600'
        
        return response
        
    except Exception as e:
        raise Http404("Error serving media file")