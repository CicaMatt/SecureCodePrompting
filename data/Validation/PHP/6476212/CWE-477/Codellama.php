<?php
$source = file_get_contents($link);
file_put_contents(' /img/uploads/' . $iconfilename, $source);
?>