async function buscarPrevisao(event) {
  event.preventDefault();

  const local = document.getElementById("local").value;
  const dt_begin = document.getElementById("dt_begin").value;
  const dt_end = document.getElementById("dt_end").value;

  console.log(local,dt_begin,dt_end);

  try {
    const response = await fetch('/api/weather', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        local: local,
        dt_begin: dt_begin,
        dt_end: dt_end
      })
    });

    if (response.ok) {
      const data = await response.json();
      console.log("API Response:", data);

      if (data.error) {
        Swal.fire({
          title: 'Erro!',
          text: data.error,
          icon: 'error',
          confirmButtonText: 'Ok'
        });
        return;
      }

      let weatherInfo = '';
      data.forecast.forEach(day => {
        weatherInfo += `
          <strong>${day.date}</strong><br>
          ${day.description} <br>
          Mín: ${day.temp_min}°C | Máx: ${day.temp_max}°C
          <br><img src="https://openweathermap.org/img/wn/${day.icon}@2x.png">
          <hr>
        `;
      });

      const result = await Swal.fire({
        title: 'Previsão do Tempo',
        html: weatherInfo,
        icon: 'info',
        showCancelButton: false,
        confirmButtonText: 'Fechar',
        focusCancel: true,
        reverseButtons: true,
      });
    } else {
      throw new Error('Falha na requisição da previsão do tempo');
    }
  } catch (error) {
    console.error("Erro ao buscar previsão do tempo:", error);
    Swal.fire({
      title: 'Erro!',
      text: 'Erro ao buscar previsão do tempo. Tente novamente.',
      icon: 'error',
      confirmButtonText: 'Ok'
    });
  }
}

// Adicionando o evento de click para o botão de Consultar Previsão
document.getElementById("consultarPrevisao").addEventListener("click", buscarPrevisao);