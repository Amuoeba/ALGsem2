
public class ExtPoint extends Point implements Comparable<ExtPoint>{
		
		static private Point p0 = null;
		
		ExtPoint(double x_value, double y_value){
			super(x_value, y_value);
		}
		
		ExtPoint(Point p){
			super(p.x, p.y);
		}
		
		public void setP0(Point p) {
			p0 = p;
		}
		
		@Override
	    public int compareTo(ExtPoint that){
			//TODO: Primerjanje kota točk this and that glede na točko p0
			return 0;
			
	    }
		
		public String toString() {
			return this.x + ", " + this.y + "-" + p0.x + ", "+ p0.y;
		}
	}