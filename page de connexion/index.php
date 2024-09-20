<?php
$connexion = new PDO('mysql:host=127.0.0.1;dbname=test_rh_sbin','root','');
if(isset($_POST['valider'])){
    if(!empty($_POST['username']) and !empty($_POST['password'])){
        $username = htmlspecialchars($_POST['username']);
        $password = $_POST['password'];
        $req = $connexion->prepare("SELECT *FROM utilisateur WHERE username =? and password = ?");
        $req->execute(array($username,$password));
        $cpt = $req->rowCount();

        if ($cpt==1){
            header('Location:http://localhost:8501/');
        }else{
            $message = "Désolé, nous ne trouvons pas ce compte";
        }
        
    }else{
        $message = "Remplissez tous les champs";
    }
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        *{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family:Arial, Helvetica, sans-serif;
        }
        html{
            height: 100%;
            width: 100%;
        }
        body{
            height: 100%;
            width: 100%;
        }
        .container{
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 100%;
            width: 100%;
        }
        .image{
            height: 100%;
            width: 50%;
        }
        .image img{
            height: 100%;
            width: 100%;
            object-fit: cover;
        }
        .connexion{
            display: flex;
            align-items: center;
            flex-direction: column;
            height: 100%;
            width: 50%;
        }
        .connexion .logo{
            margin: 10% 0;
        }
        .connexion .informations{
            display: flex;
            flex-direction: column;
            height: 50%;
            width: 65%;
        }
        .connexion .informations .name p{
            margin-bottom: 5%;
        }
        .connexion .informations .name input{
            padding: 15px 0;
            width: 100%;
            border: none;
            background-color: rgb(245, 245, 245);
            outline: 0;
        }
        .connexion .informations .password p{
            margin-top: 13%;
            margin-bottom: 5%;
        }
        .connexion .informations .password input{
            padding: 15px 0;
            width: 100%;
            border: none;
            background-color: rgb(245, 245, 245);
            outline: 0;
        }
        .connexion .informations .submit{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 23%;
        }
        .connexion .informations .submit .lien a{
            text-decoration: none;
        }
        .connexion .informations .submit .validation{
            border: solid 1px #9cca30;
            padding: 10px 30px;
            background-color: #9cca30;
            color: #000;
            text-decoration: none;
        }
        .connexion .informations .submit .validation:hover{
            cursor: pointer;
            transition: 0.5s ease-out;
            background-color: #fff;
            color: #9cca30;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="image">
            <img src="https://img.freepik.com/photos-gratuite/agence-marketing-authentique-petite-jeune_23-2150167353.jpg">
        </div>
        <div class="connexion">
            <div class="logo">
                <img src="data:image/jpeg;base64,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">
            </div>
            <div class="informations">
                <form action="" method="post">
                    <div class="name">
                        <p>Nom de l'utilisateur</p>
                        <input type="text" name="username">
                    </div>
                    <div class="password">
                        <p>Mot de passe</p>
                        <input type="password" name="password">
                    </div>
                    <div class="submit">
                        <div class="lien">
                            <a href="" target="_blank">Mot de passe oublié ?</a>
                        </div>
                        <button class="validation" type="buton" name="valider">Valider</button>
                    </div>
                    <i style="color:red; justify-content:center">
                        <?php
                            if(isset($message)){
                                echo $message."<br />";
                            }
                        ?>
                    </i>
                </form>
                
            </div>
        </div>
    </div>
</body>
</html>


