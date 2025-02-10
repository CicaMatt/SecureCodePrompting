<?php
// Enable caching for GET requests
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $cache = new Cache(); // Create a cache object
    $response = $cache->get($cache_key); // Retrieve the cached response (if any)
    if (!$response) {
        // Generate and store the response in the cache
        $response = generate_response();
        $cache->set($cache_key, $response);
    }
    echo $response; // Output the cached response
} else {
    // Handle non-GET requests normally
    handle_non_get_request();
}