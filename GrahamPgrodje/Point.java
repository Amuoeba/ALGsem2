public class Point{
	public double x;
	public double y;
	
	Point(double x_value, double y_value){
		x = x_value;
		y = y_value;
	}
	
	public String toString() {
		return "("+x+", "+y+")";
	}
}