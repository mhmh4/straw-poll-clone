<?php

function get_pdo()
{
    $dsn = "";
    $username = "root";
    $password = "";

    try {
        $pdo = new PDO($dsn, $username, $password);
    } catch (PDOException $exception) {
        echo "";
    }

    return $pdo;
}

function poll_id_exists($poll_id)
{
    $pdo = get_pdo();
    $statement = $pdo->prepare("SELECT * FROM polls WHERE poll_id = ?");
    $statement->execute(array($poll_id));
}

function create_poll($question, $options)
{
    $pdo = get_pdo();
    $sql = "INSERT INTO polls (question, options, votes) VALUES (?, ?, ?)";

    $statement = $pdo->prepare($sql);
    $statement->execute(array($question, $options));
}

function update_poll($poll_id, $option_number)
{}

function is_poll_expired()
{}

function delete_poll()
{}
