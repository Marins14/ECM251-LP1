public class Lagarto extends Jogada {

    public Lagarto() {
        super(EnumJogadas.SPOKE, EnumJogadas.PAPEL);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.LAGARTO;
    }
    
}