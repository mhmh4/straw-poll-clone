<?php

require 'functions.php';

$poll_id = $_GET['id'] ?? null;


if (isset($poll_id)) {

}

?>

<?php

$question = $_POST['question'] ?? null;
$options = $_POST['option'] ?? null;

if (isset($question, $options)) {

  var_dump($options);

  // header("Location: ");
}

?>

<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Straw Poll</title>

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
