Code Snippet:
<?php
// Use safe password hashing instead of hard-coded credentials
$hash = password_hash("password123", PASSWORD_DEFAULT); // Generate a hash for a password using the default algorithm
echo $hash; // Output the hash value

// Save an image from URL to folder on server
function GetImageFromUrl($link) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_POST, 0);
    curl_setopt($ch, CURLOPT_URL, $link);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
$sourcecode = GetImageFromUrl("http://example.com/image.jpg"); // Get image from URL
$savefile = fopen(' /img/uploads/' . $iconfilename, 'w'); // Create a new file with the desired filename and path
fwrite($savefile, $sourcecode); // Write the source code to the file
fclose($savefile); // Close the file handle
echo "Image saved successfully.";