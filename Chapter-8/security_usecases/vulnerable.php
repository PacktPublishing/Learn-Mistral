<?php
if (isset($_GET['input'])) {
    $input = $_GET['error']; 
    echo "<div>Error: $input</div>"; 
} else {
    echo "<div>No input provided.</div>";
}
?>