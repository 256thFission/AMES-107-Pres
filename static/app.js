setInterval(function () {
  try {
    fetch('/api/status').then(function (r) { return r.json(); }).then(function (d) {
      var b = document.body;
      if (String(d.stage) !== b.dataset.stage ||
          String(d.voting_open) !== b.dataset.votingOpen ||
          String(d.results_visible) !== b.dataset.resultsVisible ||
          String(d.revealed) !== b.dataset.revealed) {
        location.reload();
      }
    }).catch(function () {});
  } catch (e) {}
}, 2500);
