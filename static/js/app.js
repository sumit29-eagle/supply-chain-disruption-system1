const $ = (id) => document.getElementById(id);
async function loadOverview() {
  try {
    const response = await fetch('/api/overview');
    const data = await response.json();
    $('orders').textContent = data.metrics.total_orders;
    $('delayed').textContent = data.metrics.delayed_shipments;
    $('lowstock').textContent = data.metrics.low_stock_items;
    $('suppliers').textContent = data.metrics.at_risk_suppliers;
    $('shipment-rows').innerHTML = data.shipments.map(s => `<tr><td>${s.id}</td><td>${s.route}</td><td><span class="status ${s.status === 'Delayed' ? 'status-delayed' : 'status-on-time'}">${s.status}</span></td><td>${s.eta}</td></tr>`).join('');
    $('inventory-rows').innerHTML = data.inventory.map(i => {
      const low = i.stock <= i.reorder_level;
      const pct = Math.min(100, Math.round(i.stock / (i.reorder_level * 2) * 100));
      return `<div><div class="stock-head"><b>${i.item}</b><span>${i.stock} ${i.unit}</span></div><div class="bar"><span class="${low ? 'low' : ''}" style="width:${pct}%"></span></div>${low ? `<div class="stock-note">Below reorder level (${i.reorder_level})</div>` : ''}</div>`;
    }).join('');
  } catch (error) {
    console.error('Could not load dashboard data', error);
  }
}
$('analysis-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  const button = $('analyze-btn');
  const result = $('analysis-result');
  button.disabled = true;
  button.textContent = 'Analyzing…';
  result.classList.remove('hidden');
  result.innerHTML = '<p>Agents are reviewing the disruption…</p>';
  try {
    const response = await fetch('/api/analyze', {
      method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({disruption: $('disruption').value})
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Analysis failed');
    result.innerHTML = `<h3>Analysis summary</h3><p>${escapeHtml(data.summary)}</p><h3>Recommended actions</h3><ul>${data.recommended_actions.map(a => `<li>${escapeHtml(a)}</li>`).join('')}</ul><h3>Agent findings</h3><div class="agent-results">${data.agents.map(a => `<div class="agent-result"><b>${escapeHtml(a.agent)}</b><p>${escapeHtml(a.finding || a.recommendation || a.recommendations?.join(' ') || a.note || JSON.stringify(a))}</p></div>`).join('')}</div><p><small>${escapeHtml(data.disclaimer)}</small></p>`;
  } catch (error) {
    result.innerHTML = `<p>${escapeHtml(error.message)}</p>`;
  } finally {
    button.disabled = false;
    button.innerHTML = 'Run analysis <span>→</span>';
  }
});
function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}
loadOverview();
