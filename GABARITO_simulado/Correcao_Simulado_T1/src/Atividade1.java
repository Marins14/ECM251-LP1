public class Atividade1 {
    public static void run(){
        Usuario usuario1 = new Usuario("all might", "123", "deus@gmail.com");
        Usuario usuario2 = new Usuario("Geralt", "1234", "deus2@gmail.com");
        Usuario usuario3 = new Usuario("One For all", "1235", "deus3@gmail.com");

        usuario1.getConta().depositar(1000);
        usuario2.getConta().depositar(250);
        usuario3.getConta().depositar(3000);
        
        String qrCode1=Transacoes.gerarQrCode(usuario1.getConta().getIdConta(),usuario1.getNome(),250);

        System.out.println("Transacao 1:"+ usuario2.getConta().transferir(extrairValorQrCode(qrCode1),usuario1.getConta()));
        System.out.println("Transacao 2:"+ usuario3.getConta().transferir(extrairValorQrCode(qrCode1),usuario1.getConta()));
        System.out.println("Transacao 3:"+ usuario2.getConta().transferir(extrairValorQrCode(qrCode1),usuario1.getConta()));

        String qrCode2=Transacoes.gerarQrCode(usuario2.getConta().getIdConta(),usuario2.getNome(),1000);
        

    }

    private static double extrairValorQrCode(String qrCode){
        return Double.parseDouble(qrCode.split(";")[2]);
    }
}
