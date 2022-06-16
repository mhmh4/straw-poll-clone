<?php

function get_pdo() : PDO
{
    $dsn = "mysql:dbname=straw_poll_clone;host=localhost";
    $username = "root";
    $password = "";

    try {
        $pdo = new PDO($dsn, $username, $password);
    } catch (PDOException $exception) {
        $error_message = $exception->getMessage();
        echo $error_message;
        exit(1);
    }

    return $pdo;
}

function doesPollExist($poll_id) : bool
{
    $pdo = get_pdo();
    $sql = "SELECT * FROM polls WHERE poll_id = ?";

    $statement = $pdo->prepare($sql);
    $statement->execute(array($poll_id));

    return $statement->rowCount() == 1;
}

function getPoll($poll_id)
{
    $pdo = get_pdo();
    $sql = "SELECT * FROM polls WHERE poll_id = ?";

    $statement = $pdo->prepare($sql);
    $statement->execute(array($poll_id));

    $row = $statement->fetch();
    return $row;
}

function createPoll($question, $options, $allow_multiple_answers)
{
    // Filter out empty values and whitespace values from `options`.
    $options = array_filter(
        $options,
        fn($value) => !is_null($value) && $value !== '' && !ctype_space($value)
    );
    $options_json = json_encode($options);

    $num_options = count($options);

    // If there are n options, then there must be n fields that stores
    // the votes for those options.
    $votes = array_map(fn() => 0, range(1, $num_options));
    $votes_json = json_encode($votes);

    $pdo = get_pdo();
    $sql = 'INSERT INTO polls (question, options, votes, allow_multiple_answers) VALUES (?, ?, ?, ?)';

    $statement = $pdo->prepare($sql);
    $statement->execute(array($question, $options_json, $votes_json, $allow_multiple_answers));

    // $row = $statement->fetch();
    // return $row['poll_id'];
}

function updatePoll($poll_id, $option_number) {}

function isPollExpired($poll) {}

function deletePoll($poll) {}
