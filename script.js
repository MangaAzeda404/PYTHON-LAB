'use strict';
const state = { modules: [], selected: null };
const el = id => document.getElementById(id);
const fmt = n => new Intl.NumberFormat('pt-BR', {maximumFractionDigits: 8}).format(n);
function evaluate(id, v) {
  const sum = a => a.reduce((x,y) => x+y,0);
  let result, detail;
  switch(id) {
    case 'esmaltes': result = `Luiza tem ${fmt(sum(v))} esmaltes.`; detail = `${fmt(v[0])} + ${fmt(v[1])} + ${fmt(v[2])} = ${fmt(sum(v))}`; break;
    case 'pontos': result = `A pontuação total de Pedro é ${fmt(3*v[0]+5*v[1])}`; detail = `Corrida: ${fmt(3*v[0])} pontos · Natação: ${fmt(5*v[1])} pontos`; break;
    case 'jogos': result = `Cada amigo recebe ${fmt(Math.floor(v[0]/v[1]))} jogos.`; detail = `Restam ${fmt(v[0]%v[1])} jogos. ${v[0]%v[1] === 0 ? 'A divisão é exata.' : 'A divisão tem sobra.'}`; break;
    case 'idade': result = `Daqui a ${fmt(v[1])} anos, você terá ${fmt(sum(v))} anos.`; detail = `${fmt(v[0])} + ${fmt(v[1])} = ${fmt(sum(v))}`; break;
    case 'triangulo': result = `A área do triângulo é ${fmt(v[0]*v[1]/2)} unidades².`; detail = `(${fmt(v[0])} × ${fmt(v[1])}) ÷ 2 = ${fmt(v[0]*v[1]/2)}`; break;
    case 'carrinho': result = sum(v)<=20 ? 'Os itens cabem no carrinho.' : 'Os itens excedem o peso permitido.'; detail = `Peso total: ${fmt(sum(v))} kg · Limite: 20 kg`; break;
    case 'cinema': result = v[0]<=100 ? 'Todos podem entrar.' : 'O grupo excede a capacidade.'; detail = `${fmt(v[0])} pessoas · Capacidade: 100 pessoas`; break;
    default: throw new Error('Experiência não encontrada.');
  }
  if (v.some(x => !Number.isFinite(x)) || (id !== 'jogos' && !Number.isFinite(id === 'triangulo' ? v[0]*v[1]/2 : sum(v)))) throw new Error('Os valores são muito grandes para este exemplo.');
  return {result, detail};
}
function validateValues(module, values) {
  if(!Array.isArray(values) || values.length!==module.fields.length) throw new Error('Preencha todos os valores da experiência.');
  return values.map((value,i)=>{
    const [key,label,,type]=module.fields[i];
    if(typeof value !== 'number' || !Number.isFinite(value)) throw new Error(`Informe um número válido em “${label}”.`);
    if(value<0 || ((type==='positive'||type==='measure')&&value===0)) throw new Error(`“${label}” deve ser ${type==='positive'||type==='measure' ? 'maior que zero' : 'não negativo'}.`);
    if((type==='int'||type==='positive')&&!Number.isSafeInteger(value)) throw new Error(`“${label}” deve ser um inteiro válido.`);
    if(value>1e9) throw new Error(`Use no máximo 1 bilhão em “${label}”.`);
    return value;
  });
}
function displayResult(module, values){
  const r=evaluate(module.id,validateValues(module,values));
  el('result').textContent=r.result;el('detail').textContent=r.detail;el('error').hidden=true;
  return r;
}
function selectModule(id){
  const m=state.modules.find(m=>m.id===id);if(!m)throw new Error('Experiência não encontrada.');state.selected=m;
  document.querySelectorAll('.module-button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.id===id)));
  el('category').textContent=m.category.toUpperCase();el('experimentTitle').textContent=m.title;el('description').textContent=m.desc;
  el('explanation').textContent=m.explain;el('code').textContent=m.code;el('copyCode').textContent='Copiar código';
  el('steps').replaceChildren(...m.steps.map(text=>{const li=document.createElement('li');li.textContent=text;return li;}));
  el('fields').replaceChildren(...m.fields.map(([key,label,value,type])=>{
    const div=document.createElement('div');div.className='field';
    const l=document.createElement('label');l.htmlFor=key;l.textContent=label;
    const input=document.createElement('input');input.id=key;input.name=key;input.type='number';input.value=value;input.required=true;
    input.min=type==='positive'?1:type==='measure'?0.00000001:0;input.max=1e9;input.step=type==='int'||type==='positive'?'1':'any';
    div.append(l,input);return div;
  }));displayResult(m,m.fields.map(f=>f[2]));
}
el('calcForm').addEventListener('submit',e=>{
  e.preventDefault();if(!state.selected)return;
  try{const values=state.selected.fields.map(f=>el(f[0]).valueAsNumber);displayResult(state.selected,values);}
  catch(err){el('error').textContent=err.message;el('error').hidden=false;el('result').textContent='Revise os valores.';el('detail').textContent='';}
});
el('copyCode').addEventListener('click',async()=>{
  if(!state.selected)return;
  try{await navigator.clipboard.writeText(state.selected.code);el('copyCode').textContent='Copiado!';}
  catch{const selection=window.getSelection();const range=document.createRange();range.selectNodeContents(el('code'));selection.removeAllRanges();selection.addRange(range);el('copyCode').textContent='Selecione e copie';}
});
function registerTools(){
  const ctx=document.modelContext;if(!ctx?.registerTool)return;
  const controller=new AbortController();window.addEventListener('pagehide',()=>controller.abort(),{once:true});
  try{Promise.resolve(ctx.registerTool({name:'calculate_python_example',title:'Calcular um exemplo do laboratório',description:'Seleciona uma das sete experiências, aplica os valores numéricos na ordem dos campos e mostra o cálculo na página.',inputSchema:{type:'object',properties:{experiment:{type:'string',enum:state.modules.map(m=>m.id)},values:{type:'array',items:{type:'number'},minItems:1,maxItems:3}},required:['experiment','values'],additionalProperties:false},annotations:{readOnlyHint:false,untrustedContentHint:false},execute(input){
    if(!input||typeof input!=='object'||Object.keys(input).some(k=>!['experiment','values'].includes(k)))throw new Error('Entrada inválida.');
    const m=state.modules.find(m=>m.id===input.experiment);if(!m)throw new Error('Experiência não encontrada.');
    const values=validateValues(m,input.values);const result=evaluate(m.id,values);selectModule(m.id);m.fields.forEach((f,i)=>el(f[0]).value=values[i]);displayResult(m,values);return {experiment:m.id,...result};
  }},{signal:controller.signal})).catch(()=>{});}catch{}
}
fetch('modules.json').then(r=>{if(!r.ok)throw new Error();return r.json();}).then(modules=>{
  state.modules=modules;
  el('moduleList').replaceChildren(...modules.map(m=>{const b=document.createElement('button');b.type='button';b.className='module-button';b.dataset.id=m.id;b.setAttribute('aria-pressed','false');b.setAttribute('aria-controls','experimentTitle');
    const number=document.createElement('span');number.className='num';number.textContent=m.icon;
    const text=document.createElement('span');const title=document.createElement('b');title.textContent=m.title;const sub=document.createElement('small');sub.textContent=m.category;text.append(title,sub);b.append(number,text);b.addEventListener('click',()=>selectModule(m.id));return b;}));
  selectModule(modules[0].id);registerTools();
}).catch(()=>{el('description').textContent='Não foi possível carregar as experiências. Recarregue a página ou baixe o programa Python.';el('category').textContent='FALHA NO CARREGAMENTO';el('calcForm').hidden=true;});
