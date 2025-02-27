{% extends 'base.html' %}

{% block title %}
  Produtos
{% endblock %}

{% block css %} 

  <style>
    body {
      background-color: #1d7fe0;
      padding: 20px;
    }

    form {
      max-width: 400px;
      margin: auto;
      background-color: #c7ec0a;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    h2 {
      margin-bottom: 20px;
      color: #007bff; 
    }

    label {
      color: #495057; 
    }

    button {
      background-color: #007bff;
      color: #ffffff;
      border: none;
    }

    button:hover {
      background-color: #0056b3; 
    }
  </style>
{% endblock %}

{% block conteudo %}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.2/font/bootstrap-icons.min.css">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

  <h2 class="text-center">Produtos</h2>
  <form id="prodForm" action="YOUR_FORM_ACTION_URL" method="post">
    <div class="mb-3">
        <label for="nome" class="form-label">Nome:</label>
        <input type="text" class="form-control" id="nome" name="nome" placeholder="Nome" required>
    </div>

    <div class="mb-3">
        <label for="descricao" class="form-label">Descrição:</label>
        <textarea class="form-control" id="descricao" name="descricao" placeholder="Descrição" maxlength="255"></textarea>
    </div>

    <div class="mb-3">
        <label for="preco" class="form-label">Preço:</label>
        <input type="text" class="form-control" id="preco" name="preco" placeholder="Preço">
    </div>

    <div class="text-center">
      <h4 style="color: #007bff;">Para finalizar a compra, será feita pelo WhatsApp</h4>
      <button type="submit" class="btn btn-primary"><i class="bi bi-whatsapp"></i> Whatsapp</button>
    </div>
  </form>
{% endblock %}
