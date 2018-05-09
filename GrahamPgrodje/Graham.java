import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.Stack;

public class Graham {
	public static void main(String[] args) {
		//Random tester
		//Point[] tocke = generateData(15,1236);
		
		Point[] tocke = new Point[5];
		tocke[0] = new Point(0,0);
		tocke[1] = new Point(1,0);
		tocke[2] = new Point(1,1);
		tocke[3] = new Point(0,1);
		tocke[4] = new Point(0.5,0.5);
		
		System.out.println("Vhodne točke:");
		for(Point p : tocke)
			System.out.println(p);
	
		tocke = grahmScan(tocke);
		
		System.out.println("Konveksna ovojnica:");
		for(Point p : tocke) {
			System.out.println(p);
		}

	}
	
	public static Point[] grahmScan(Point[] tocke) {
		List<ExtPoint> urejeneTocke = new ArrayList<ExtPoint>();
		//Najdi najnižjo točko p0, glede na y ter nato na x
		//Uredi vse točke glede na kot od p0 v nasprotni smeri urinega kazalca
		//Uporabite Graham scan za iskanje konveksne ovojnice
		
		return null;
	}
	
	/*
	 * Relativna smer daljice ij glede na daljico ik
	 * return: 
	 * 0 -> Daljici sta vzporedni -> ToÃ¨ke so kolinearne
	 * + -> Daljica ij leÅ¾i desno od ik
	 * - -> Daljica ij leÅ¾i levo od ik
	 */
	private static double Direction(ExtPoint i, ExtPoint j, ExtPoint k){
		double x1 = k.x - i.x;
		double y1 = k.y - i.y;
		double x2 = j.x - i.x;
		double y2 = j.y - i.y;
		return x1*y2-y1*x2;
	}
	
	/*
	 * Generator testnih podatkov. ToÄ�ke so vedno vrnjene v okviru (0,0) do (1000, 1000)
	 */
	public static Point[] generateData(int tock, int seed){
		if(tock < 3) {
			System.out.println("Å tevilo toÄ�k mora biti vsaj 3.");
			System.exit(0);
		}

		Point[] seznam = new Point[tock];
		Random generator = new Random(seed);
		for(int i = 0; i < tock; i++) {
			double x = generator.nextDouble()*1000;
			double y = generator.nextDouble()*1000;
			seznam[i] = new Point(x,y);
		}
		
		return seznam;
	}
}
