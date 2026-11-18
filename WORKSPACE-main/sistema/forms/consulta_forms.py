class ConsultaForm(forms.ModelForm):
    class Meta:
        model = consulta
    # ... (campos, Meta, __init__ e clean_cpf_paciente da Apostila 01) ...

    # ── NOVO: data no passado não pode (só ao criar; editar consulta antiga é permitido)
    def clean_horario(self):
        horario = self.cleaned_data['horario']
        if not self.instance.pk and horario < timezone.now():
            raise forms.ValidationError('Escolha uma data e hora que ainda não passou.')
        return horario

    # ── NOVO: clean() valida campos EM CONJUNTO (roda depois de todos os clean_<campo>)
    def clean(self):
        dados = super().clean()
        medico = dados.get('medico_id')      # .get(): o campo pode ter falhado antes
        horario = dados.get('horario')

        if medico and horario:
            ocupado = Consulta.objects.filter(medico_id=medico, horario=horario)
            ocupado = ocupado.exclude(pk=self.instance.pk).exclude(status='X')
            if ocupado.exists():
                # add_error(campo, mensagem): o erro aparece embaixo do campo "horario"
                self.add_error('horario', f'{medico} já tem uma consulta neste horário.')

        return dados

    # ... (save() da Apostila 01, sem mudanças) ...