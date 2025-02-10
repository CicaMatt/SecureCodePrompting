<?php
// Set the cache limiters and expiration time
session_cache_limiter('public'); // Allow caching for all users
session_cache_expire(180); // Expire the cache after 180 seconds

// Set the content type and language headers
header("Content-type: $documentMimeType; charset=$documentCharset");
header('Vary: Accept');
header("Content-language: $currentLanguage");