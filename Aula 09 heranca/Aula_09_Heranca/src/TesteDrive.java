public class TesteDrive {
    public static void executar(){
        System.out.println("dado generico");
        Dado d1 = new Dado("123");
        System.out.println("Dado Criado: " +d1 );
        System.out.println("Face Atual: "+ d1.faceAtual());
        //Sorteia uma nova face 
        d1.rodar();
        System.out.println("Face Atual: "+ d1.faceAtual());

        System.out.println("DadoD6");
        Dado d2 = new DadoD6("1234");
        System.out.println("Dado Criado: " +d2 );
        System.out.println("Face Atual: "+ d2.faceAtual());
        //Sorteia uma nova face 
        d2.rodar();
        System.out.println("Face Atual: "+ d2.faceAtual());

        System.out.println("DadoD10");
        Dado d3 = new DadoD10("123456");
        System.out.println("Dado Criado: " +d3 );
        System.out.println("Face Atual: "+ d3.faceAtual());
        //Sorteia uma nova face 
        d3.rodar();
        System.out.println("Face Atual: "+ d3.faceAtual());

        System.out.println("DadoD20");
        Dado d4 = new DadoD20("1234567");
        System.out.println("Dado Criado: " +d4 );
        System.out.println("Face Atual: "+ d4.faceAtual());
        //Sorteia uma nova face 
        d4.rodar();
        System.out.println("Face Atual: "+ d4.faceAtual());
    }
}
