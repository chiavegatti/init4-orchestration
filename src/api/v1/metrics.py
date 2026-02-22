from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime

from src.db.session import get_db
from src.models.request import RequestLog

router = APIRouter()


@router.get("/")
def get_metrics_summary(db: Session = Depends(get_db)):
    """
    Returns a high-level summary of usage and cost metrics for the dashboard.
    """
    total_requests = db.query(RequestLog).count()
    total_cost = db.query(func.sum(RequestLog.estimated_cost)).scalar() or 0.0

    # Model breakdown
    models = (
        db.query(
            RequestLog.routed_model,
            func.count(RequestLog.id).label("request_count"),
            func.sum(RequestLog.estimated_cost).label("cost"),
        )
        .group_by(RequestLog.routed_model)
        .all()
    )

    model_stats = {
        item.routed_model: {
            "request_count": item.request_count,
            "cost": float(item.cost) if item.cost else 0.0,
        }
        for item in models
    }

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "total_requests": total_requests,
        "total_estimated_cost_usd": float(total_cost),
        "models": model_stats,
    }
