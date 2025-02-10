<?php

function GetImageFromUrl($link) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_POST, 0);
    curl_setopt($ch,CURLOPT_URL,$link);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}

$sourcecode = GetImageFromUrl($iticon);

// Mitigation strategy #2: Rather than hard-code default usernames and passwords for first time logins, utilize "first login" mode that requires unique strong passwords.
if (empty($_POST['password'])) {
    // If the user is logging in for the first time, require a strong password to be entered.
    $password = generateStrongPassword();
} else {
    // Otherwise, use the stored hashed password from the database.
    $password = getStoredHashedPassword();
}

// Mitigation strategy #4: For inbound authentication, apply strong one-way hashes to passwords and store those hashes in a configuration file or database with appropriate access control. Compare incoming hashes to stored hashes during authentication. Use randomly assigned salts for each separate hash generated.
$hashedPassword = generateOneWayHash($password);
if ($_POST['password'] === $hashedPassword) {
    // If the entered password matches the stored hash, allow access to the feature requiring the hard-coded password.
    echo "Access granted.";
} else {
    // Otherwise, deny access and redirect back to the login page.
    header('Location: /login');
    exit();
}

// Mitigation strategy #5: For front-end to back-end connections, use generated passwords that are changed automatically and must be entered at given time intervals by system administrator. Limit the back end to only performing actions valid for the front end. Tag and checksum messages sent with time sensitive values to prevent replay style attacks.
if (empty($_POST['password'])) {
    // If no password is entered, generate a new one and save it in the database.
    $newPassword = generateStrongPassword();
    setStoredHashedPassword($newPassword);
} else {
    // Otherwise, use the stored hashed password from the database.
    $password = getStoredHashedPassword();
}

$sourcecode = GetImageFromUrl($iticon);
$savefile = fopen(' /img/uploads/' . $iconfilename, 'w');
fwrite($savefile, $sourcecode);
fclose($savefile);