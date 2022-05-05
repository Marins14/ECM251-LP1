public class Papel extends Jogada {
    public Papel() {
        super(EnumJogadas.PEDRA, EnumJogadas.SPOKE);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.PAPEL;
    }
}