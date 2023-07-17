<?php
require '../assets/forms/contact.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $receiving_email_address = $_POST['profissional_email'];

  $mail = new PHPMailer;
  $mail->isSMTP();
  $mail->Host = 'smtp.example.com';  // Insira o host SMTP do seu provedor de email
  $mail->SMTPAuth = true;
  $mail->Username = 'your_email@example.com';  // Insira o seu endereço de email
  $mail->Password = 'your_password';  // Insira a senha do seu email
  $mail->SMTPSecure = 'tls';
  $mail->Port = 587;

  $mail->setFrom($_POST['email'], $_POST['name']);
  $mail->addAddress($receiving_email_address);

  $mail->isHTML(true);
  $mail->Subject = $_POST['msg_subject'];
  $mail->Body = $_POST['message'];

  if (!$mail->send()) {
    echo 'Erro ao enviar o email: ' . $mail->ErrorInfo;
  } else {
    echo 'Email enviado com sucesso!';
  }
}
?>
