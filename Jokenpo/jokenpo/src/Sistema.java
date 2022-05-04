import java.util.concurrent.ThreadLocalRandom;

public class Sistema {
    public static void rodar(){
        // usuario escolhe a jogada 
        Jogada jogada1 = new Pedra();
        //sorteio da jogada para o PC 
        Jogada jogada2 = sortearJogada();
        //avaliação das jogadas
        String resultado = avaliaJogadas(jogada1, jogada2);
        // exibição do resultado
        System.out.println("Resultado:"+ resultado);
    }

    private static Jogada sortearJogada() {
        Jogada jogadas[] = new Jogada[3];
        jogadas[0] = new Pedra();
        jogadas[1] = new Papel();
        jogadas[2] = new Tesoura();
        return jogadas[ThreadLocalRandom.current().nextInt(jogadas.length)];
    }

    private static String avaliaJogadas(Jogada jogada1, Jogada jogada2) {
        if (jogada1.verificarVenceu(jogada2))
            return "Jogada1";
        if(jogada2.verificarVenceu(jogada1))
            return "Jogada2";
        return "Empate";
    }
    
}
