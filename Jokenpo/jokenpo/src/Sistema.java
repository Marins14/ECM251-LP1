public class Sistema {
    public static void rodar(){
        // usuario escolhe a jogada 
        Jogada jogada1 = new Pedra("Tesoura");
        //sorteio da jogada para o PC 
        Jogada jogada2 = new Papel("Pedra");
        //avaliação das jogadas
        String resultado = avaliaJogadas(jogada1, jogada2);
        // exibição do resultado
        System.out.println("Resultado:"+ resultado);
    }

    private static String avaliaJogadas(Jogada jogada1, Jogada jogada2) {
        if (jogada1.verificarVenceu(jogada2))
            return "Jogada1";
        if(jogada2.verificarVenceu(jogada1))
            return "Jogada2";
        return "Empate";
    }
    
}
