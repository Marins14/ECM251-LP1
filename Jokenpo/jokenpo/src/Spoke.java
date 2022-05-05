public class Spoke extends Jogada {

    public Spoke() {
        super(EnumJogadas.TESOURA,EnumJogadas.PEDRA);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.SPOKE;
    }
    
}
