<?php

require 'functions.php';

$poll_id = $_GET['id'] ?? null;

if (isset($poll_id)) {
  // if (!doesPollExist($poll_id)) {
    // include '404.php';
    // exit(1);
  // }

  $poll = getPoll($poll_id);

  $question = $poll['question'];
  $options_json = $poll['options'];
  $options = json_decode($options_json);

  // var_dump($poll);
}

?>

<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title><?= $question ?> - Straw Poll</title>

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-5">
    <h6 class="display-6"><?= $question ?></h6>
    <div>
      <form method="post">
        <!-- Options -->
        <?php foreach(array_values($options) as $i => $option): ?>
          <div>
            <input type="radio" name="" id="<?= $i ?>" value="">
            <label for="<?= $i ?>"></label>

            <?= $option ?>
          </div>
          <?php endforeach; ?>
        </div>
        <!-- Submit button -->
        <button type="submit" class="btn btn-primary">Vote</button>
      </form>
  </div>
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
