import { useState } from "react";

import ClientForm from "../components/ClientForm";
import ClientsTable from "../components/ClientsTable";
import MembershipForm from "../components/MembershipForm";
import MembershipList from "../components/MembershipList";
import PaymentForm from "../components/PaymentForm";
import PaymentHistory from "../components/PaymentHistory";
import { useClientes } from "../hooks/useClientes";
import { useMembresias } from "../hooks/useMembresias";
import { usePagos } from "../hooks/usePagos";

export default function DashboardPage() {
  const clientesState = useClientes();
  const membresiasState = useMembresias();
  const pagosState = usePagos();
  const [submitting, setSubmitting] = useState({
    cliente: false,
    membresia: false,
    pago: false,
  });
  const [submitError, setSubmitError] = useState("");

  const handleClienteSubmit = async (payload) => {
    try {
      setSubmitError("");
      setSubmitting((current) => ({ ...current, cliente: true }));
      await clientesState.saveCliente(payload);
    } catch (error) {
      setSubmitError(error.response?.data?.detail || "No se pudo crear el cliente.");
    } finally {
      setSubmitting((current) => ({ ...current, cliente: false }));
    }
  };

  const handleMembresiaSubmit = async (payload) => {
    try {
      setSubmitError("");
      setSubmitting((current) => ({ ...current, membresia: true }));
      await membresiasState.saveMembresia(payload);
    } catch (error) {
      setSubmitError(error.response?.data?.detail || "No se pudo crear la membresia.");
    } finally {
      setSubmitting((current) => ({ ...current, membresia: false }));
    }
  };

  const handlePagoSubmit = async (payload) => {
    try {
      setSubmitError("");
      setSubmitting((current) => ({ ...current, pago: true }));
      await pagosState.savePago(payload);
      await clientesState.loadClientes();
    } catch (error) {
      setSubmitError(error.response?.data?.detail || "No se pudo registrar el pago.");
    } finally {
      setSubmitting((current) => ({ ...current, pago: false }));
    }
  };

  const globalError = submitError || clientesState.error || membresiasState.error || pagosState.error || "";

  return (
    <main className="dashboard-shell">
      <section className="hero">
        <div>
          <p className="eyebrow">Gym Olympo</p>
          <h1>Control local de membresias sin caos de papel</h1>
          <p className="hero-copy">
            Registra clientes, cobra pagos y deja que el sistema te diga quien esta activo,
            por vencer o vencido.
          </p>
        </div>
        <div className="hero-card">
          <span>{clientesState.clientes.length}</span>
          <p>clientes en base</p>
          <span>{pagosState.pagos.length}</span>
          <p>pagos registrados</p>
        </div>
      </section>

      {globalError ? <div className="alert error">{globalError}</div> : null}

      <section className="forms-grid">
        <ClientForm onSubmit={handleClienteSubmit} submitting={submitting.cliente} />
        <MembershipForm
          onSubmit={handleMembresiaSubmit}
          submitting={submitting.membresia}
        />
        <PaymentForm
          clientes={clientesState.clientes}
          membresias={membresiasState.membresias}
          onSubmit={handlePagoSubmit}
          submitting={submitting.pago}
        />
      </section>

      <section className="content-grid">
        <ClientsTable clientes={clientesState.clientes} loading={clientesState.loading} />
        <MembershipList
          membresias={membresiasState.membresias}
          loading={membresiasState.loading}
        />
      </section>

      <PaymentHistory pagos={pagosState.pagos} loading={pagosState.loading} />
    </main>
  );
}
