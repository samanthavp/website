<?php
if(isset($_POST['email'])) {
  $email_to      = "jesse.x.knight@gmail.com.com";
  $email_subject = "Raw Talk Website - Contact Message".;
}
  $name     = $_POST['name'];
  $email    = $_POST['email'];
  $comments = $_POST['comments'];
    
  $email_message = "Message from Raw Talk Website.\n\n"; 
  $email_message .= "Name: ".$name."\n";
  $email_message .= "Email: ".$email."\n";
  $email_message .= "Comments: ".$comments."\n";
 
// create email headers
$headers = 'From: '.$email."\r\n".
           'Reply-To: '.$email."\r\n" .
           'X-Mailer: PHP/' . phpversion();
@mail($email_to, $email_subject, $email_message, $headers);  
?>
 
Thanks for getting in touch! We'll get back to you as soon as possible.
 
<?php 
}
?>
