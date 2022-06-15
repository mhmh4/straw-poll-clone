<?php

require 'functions.php';

$question = $_POST['question'] ?? null;
$options = $_POST['option'] ?? null;

if (isset($question, $options)) {

  // Filter out empty values and whitespace values from `options`.
  $options = array_filter(
    $options,
    fn($value) => !is_null($value) && $value !== '' && !ctype_space($value)
  );

  // $poll_id = create_poll($question, $options);

  // header("Location: poll.php?id=$poll_id");

  // $allow_multiple_answers = $_POST['allow-multiple-answers'] ?? false;
  var_dump($options);

  $options_json = json_encode($options);
  $num_options = count($options);

  $votes = array();
  for ($i=0; $i < $num_options; $i++) {
    $votes[] = 0;
  }

  $votes_json = json_encode($votes);

  var_dump($options);
  var_dump($votes_json);

  // echo count($options);

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
  <div class="container mt-5">
    <h6 class="display-6">Straw Poll</h6>
    <form method="post">
      <!-- Question -->
      <div class="my-3">
        <input type="text" name="question" placeholder="Type your question here" required>
      </div>
      <!-- Options -->
      <div>
        <input type="text" name="option[]" class="option d-block" placeholder="Enter poll option">
        <input type="text" name="option[]" class="option d-block" placeholder="Enter poll option">
        <input type="text" name="option[]" class="option d-block" placeholder="Enter poll option">
      </div>
      <!--  -->
      <div>
        <input type="checkbox" name="allow-multiple-answers">
        <label for="">Allow multiple poll answers</label>
      </div>

      <button type="submit" class="btn btn-primary">Create Poll</button>
    </form>
  </div>
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"></script>
  <script>
    let numOptions = 3; // There are already 3 textboxes shown.
    const MAX_OPTIONS = 20;

    let options = document.getElementsByClassName('option');
    // console.log(options);
  </script>
</body>
</html>
